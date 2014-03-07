# -*- coding: utf-8 -*-
import factory
from postbox.channel.models import Transmitter, Channel, Category


# Create the transmitter
class TransmitterFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Transmitter
    FACTORY_DJANGO_GET_OR_CREATE = ("code", )

    code = u"{{ transmitter_code }}"
    uuid = u""
    slug = u"{{ transmitter_code }}"
    name = u"{{ transmitter_code }}"
    ads = u""


# Create the Channel Category
class CategoryFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Category
    FACTORY_DJANGO_GET_OR_CREATE = ("slug", )

    slug = u"other"
    slug_fr = u"autre"
    slug_en = u"other"
    slug_de = u"andere"
    name_fr = u"Autre"
    name_en = u"Other"
    name_de = u"Andere"


# Create the Channel
class ChannelFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Channel
    FACTORY_DJANGO_GET_OR_CREATE = ("uuid")

    transmitter = factory.SubFactory(TransmitterFactory)
    category = factory.SubFactory(CategoryFactory)
    code = u"all"
    uuid = u""
    title = u"Documents"
    slug = u"documents"

    summary = u""

    is_public = True


factories = [ChannelFactory]
