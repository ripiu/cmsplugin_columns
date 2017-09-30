from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

class LiquidColumnsPluginModel(CMSPlugin):
    """
    Liquid columns
    """
    
    num_columns = models.IntegerField(
        _('columns'), default=2, blank=False,
        help_text=_('How many columns for this section?')
    )
    
    def __str__(self):
        return str(self.num_columns)
    
    class Meta:
        verbose_name = _('Liquid columns')
        verbose_name_plural = _('Liquid columns')
