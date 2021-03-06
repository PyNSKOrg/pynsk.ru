from django.contrib.sites.models import Site
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_comments.models import CommentFlag
from zinnia.managers import DRAFT, HIDDEN, PUBLISHED
from zinnia.models_bases.entry import CoreEntry, ContentEntry, ExcerptEntry, ImageEntry, FeaturedEntry, AuthorsEntry, \
    TagsEntry, RelatedEntry, LeadEntry, CategoriesEntry


class Task(ContentEntry, ImageEntry, TagsEntry):
    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (HIDDEN, _('hidden')),
                      (PUBLISHED, _('published')))

    title = models.CharField(
            _('title'), max_length=255)

    status = models.IntegerField(
            _('status'), db_index=True,
            choices=STATUS_CHOICES, default=DRAFT)

    number = models.IntegerField(verbose_name=_('Task number'))

    creation_date = models.DateTimeField(
            _('creation date'),
            db_index=True, default=timezone.now,
            help_text=_("Used to build the entry's URL."))

    last_update = models.DateTimeField(
            _('last update'), default=timezone.now)

    @property
    def publication_date(self):
        """
        Return the publication date of the entry.
        """
        return self.creation_date

    @property
    def is_visible(self):
        """
        Checks if an entry is visible and published.
        """
        return self.status == PUBLISHED

    @property
    def previous_entry(self):
        """
        Returns the previous published entry if exists.
        """
        return self.previous_next_entries[0]

    @property
    def next_entry(self):
        """
        Returns the next published entry if exists.
        """
        return self.previous_next_entries[1]

    @property
    def previous_next_entries(self):
        """
        Returns and caches a tuple containing the next
        and previous published entries.
        Only available if the entry instance is published.
        """
        previous_next = getattr(self, 'previous_next', None)

        if previous_next is None:
            if not self.is_visible:
                previous_next = (None, None)
                setattr(self, 'previous_next', previous_next)
                return previous_next

            entries = list(self.__class__.published.all())
            index = entries.index(self)
            try:
                previous = entries[index + 1]
            except IndexError:
                previous = None

            if index:
                next = entries[index - 1]
            else:
                next = None
            previous_next = (previous, next)
            setattr(self, 'previous_next', previous_next)
        return previous_next

    @property
    def link(self):
        # return reverse('apps.tasks.views.TaskPage', kwargs={'pk': self.id})
        return reverse('tasks:task-detail', kwargs={'pk': self.pk})

    @property
    def get_absolute_url(self):
        return self.link

    @property
    def rss_content(self):
        return self.html_preview

    @property
    def tips(self):
        return Tip.objects.filter(task=self)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the
        the last_update field.
        """
        self.last_update = timezone.now()
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.title, self.get_status_display())

    class Meta:
        ordering = ['-number', '-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        index_together = [['creation_date'],
                          ['status', 'creation_date']]
        permissions = (('can_view_all', 'Can view all entries'),
                       ('can_change_status', 'Can change status'),
                       ('can_change_author', 'Can change author(s)'),)


class Tip(ContentEntry):
    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (HIDDEN, _('hidden')),
                      (PUBLISHED, _('published')))

    task = models.ForeignKey(Task)

    title = models.CharField(
            _('title'), max_length=255)

    status = models.IntegerField(
            _('status'), db_index=True,
            choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return "Подсказка '{}' для задачи '{}'".format(self.title, self.task.title)
