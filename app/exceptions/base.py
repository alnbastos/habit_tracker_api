from fastapi import status


class AppError(Exception):
    status_code: int = 400
    message_template: str = "Application error"

    def __init__(self, resource: str | None = None):
        self.resource = resource
        self.detail = (
            self.message_template.format(resource=resource)
            if resource
            else self.message_template
        )
        super().__init__(self.detail)


class NotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    message_template = "{resource} not found."


class AlreadyExistsError(Exception):
    status_code = status.HTTP_409_CONFLICT
    message_template = "{resource} already exists."
