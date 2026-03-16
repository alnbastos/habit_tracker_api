from fastapi import status

from .base import AppError


class FutureCheckinDateError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Checkin date cannot be in the future"
