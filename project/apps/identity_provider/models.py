from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sessions.base_session import AbstractBaseSession
from apps.identity_provider.settings import APIKEY_EXPIRE
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

def default_expiration_date():
    return (timezone.now() + APIKEY_EXPIRE)

class Session(AbstractBaseSession):
    uuid = models.UUIDField(db_index=True, default=uuid4)
    user_id = models.IntegerField(db_index=True, null=True)
    oidc_code = models.CharField(null=True, max_length=256)

    @classmethod
    def get_session_store_class(cls):
        from apps.identity_provider.session_backend import SessionStore

        return SessionStore


class ApiKey(models.Model):
    
    # Scope enumerated choices for the field 'scope'
    scopeChoices = (
        ('management', 'Management'),
        ('resource', 'Resource')
    )
    
    user = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        help_text="API key will have the same privilege groups as it's owner.",
    )
    key = models.UUIDField(null=False, blank=False, default=uuid4)
    revoked = models.BooleanField(
        null=False,
        default=False,
        help_text="If the API key is revoked, clients cannot use it.",
    )

    last_modified = models.DateTimeField(blank=True, null=True)

    # Set an expiration date for the API key
    expiry = models.DateTimeField(blank=False, null=False, default=default_expiration_date)

    scope = models.CharField(max_length=50, blank=False, null=False, choices=scopeChoices)
