from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class DeletionMarkerMixin(models.Model):
    """
    An abstract model that contains the `deletion_marker` field.
    """

    deletion_marker = models.IntegerField(
        _("Deletion Marker"), blank=True, null=True
    )

    class Meta:
        abstract = True


class HistoricalDataMixin(models.Model):
    """
    An abstract model that adds the tracking of changes to an instance.
    Contains the `history` field.
    """

    # Keeps track of changes to a record.
    # `inherit=True`` is used to allow the re-use of this mixin.
    # https://django-simple-history.readthedocs.io/en/latest/historical_model.html#allow-tracking-to-be-inherited
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    """
    An abstract model that contains the fields:
    - `created_at`
    - `updated_at`
    """

    created_at = models.DateTimeField(
        _("Created At"), blank=True, null=True, default=timezone.now
    )
    updated_at = models.DateTimeField(_("Updated At"), blank=True, null=True)

    class Meta:
        abstract = True
