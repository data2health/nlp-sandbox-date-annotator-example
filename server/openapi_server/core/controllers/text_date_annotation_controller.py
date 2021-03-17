import re

from openapi_server.models.error import Error
from openapi_server.models.text_date_annotation import TextDateAnnotation
from openapi_server.models.text_date_annotation_response import \
    TextDateAnnotationResponse


def create_text_date_annotations(text_date_annotation_request):
    """Annotate dates in a clinical note

    Return the date annotations found in a clinical note

    :rtype: TextDateAnnotations
    """
    res = None
    status = None
    try:
        note = text_date_annotation_request._note
        annotations = []
        # Adapted from https://stackoverflow.com/a/61234139
        matches = re.finditer(
            "([1-9]|0[1-9]|1[0-2])(/)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])" +
            "(/)(19[0-9][0-9]|20[0-9][0-9])", note._text)
        add_date_annotation(annotations, matches, "MM/DD/YYYY")

        matches = re.finditer(
            "([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\\.)([1-9]|0[1-9]|" +
            "1[0-2])(\\.)(19[0-9][0-9]|20[0-9][0-9])", note._text)
        add_date_annotation(annotations, matches, "DD.MM.YYYY")

        matches = re.finditer(
            "([1-9][1-9][0-9][0-9]|2[0-9][0-9][0-9])", note._text)
        add_date_annotation(annotations, matches, "YYYY")

        matches = re.finditer(
            "(January|February|March|April|May|June|July|August|" +
            "September|October|November|December)",
            note._text, re.IGNORECASE)
        add_date_annotation(annotations, matches, "MMMM")

        res = TextDateAnnotationResponse(annotations)
        status = 200
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def add_date_annotation(annotations, matches, date_format):
    """
    Converts matches to TextDateAnnotation objects and adds them to the
    annotations array specified.
    """
    for match in matches:
        annotations.append(TextDateAnnotation(
            start=match.start(),
            length=len(match[0]),
            text=match[0],
            date_format=date_format,
            confidence=95.5
        ))
