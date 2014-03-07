# -*- coding: utf-8 -*-
import factory
from postbox.channel.models import Transmitter, Channel, Category


# Create the transmitter
class TransmitterFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Transmitter
    FACTORY_DJANGO_GET_OR_CREATE = ("code", )

    code = u"{{ cookiecutter.repo_name }}"
    uuid = u""
    slug = u"{{ cookiecutter.repo_name }}"
    name = u"{{ cookiecutter.repo_name }}"
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
    code = u"{{ cookiecutter.channel_code }}"
    uuid = u""
    title = u"{{ cookiecutter.channel_code }}"
    slug = u"{{ cookiecutter.channel_code }}"

    summary = u""

    is_public = True


factories = [ChannelFactory]
