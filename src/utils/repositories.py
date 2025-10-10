from abc import ABC
from typing import (
    Any,
    Generic,
    Iterable,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    List,
)
from django.db import models
from src.utils.functions import raise_validation_error
from src.utils.types import TModel, TDto, TQuerySet


class AbstractFetchRepository(Generic[TModel]):
    model: Type[TModel]
    dto_class: Type[TDto]

    @property
    def table_name(self) -> str:
        return self.model._meta.db_table
    
    def __to_dto(self, instance: TModel) -> TDto:
        return self.dto_class.model_validate(instance)
    
    def __to_dto_list(self, instances: List[TModel]) -> List[TDto]:
        return [self.__to_dto(i) for i in instances]

    def get(self, *args, **kwargs) -> Union[TDto, None]:
        res = self.filter(*args, **kwargs)
        if res.count() > 1:
            raise_validation_error("Multiple objects found")
        instance: TModel = res.first()
        return self.__to_dto(instance=instance) if instance else None

    def filter(self, *args, **kwargs) -> List[TDto]:
        qs: TQuerySet = self.model.objects.filter(*args, **kwargs)
        return self.__to_dto_list(list(qs))

    def all(self) -> List[TDto]:
        qs: TQuerySet = self.model.objects.all()
        return self.__to_dto_list(list(qs))

    def count(self, *args, **kwargs) -> int:
        return self.filter(*args, **kwargs).count()

    def exists(self, *args, **kwargs) -> bool:
        return self.model.objects.filter(*args, **kwargs).exists()
    
    def filter_values(
            self,
            dto_class: TDto,
            fields: Optional[List[str]] = None,
            **filters
        ):
        qs = self.model.objects.filter(**filters)
        if fields:
            qs = qs.values(fields)
        data_list = list(qs)
        return [dto_class.model_validate(d) for d in data_list]

class AbstractEditRepository(Generic[TModel]):
    model: Type[TModel]
    dto_class: Type[TDto]

    def __to_dto(self, instance: TModel) -> TDto:
        return self.dto_class.model_validate(instance)

    def create(self, **kwargs) -> TDto:
        instance = self.model.objects.create(**kwargs)
        return self.__to_dto(instance)

    def update_or_create(
        self, defaults: Optional[MutableMapping[str, Any]] = None, **kwargs
    ) -> Tuple[TDto, bool]:
        instance, created = self.model.objects.update_or_create(defaults=defaults, **kwargs)
        return self.__to_dto(instance), created

    def get_or_create(
        self, defaults: Optional[MutableMapping[str, Any]] = None, **kwargs
    ) -> Tuple[TDto, bool]:
        instance, created = self.model.objects.get_or_create(defaults=defaults, **kwargs)
        return self.__to_dto(instance), created

    @staticmethod
    def update(instance: TModel, **kwargs) -> TModel:
        instance.save(**kwargs)
        return instance

    @staticmethod
    def delete(instance: TModel):
        instance.delete()

    @staticmethod
    def save(instance: TModel, **kwargs):
        instance.save(**kwargs)

    def bulk_create(self, instances: Iterable[TModel], **kwargs) -> List[TDto]:
        objs = self.model.objects.bulk_create(instances, **kwargs)
        return [self.dto_class.model_validate(o) for o in objs]

    def bulk_update(
        self,
        instances: Iterable[TModel],
        fields: Sequence[str],
        batch_size: Optional[int],
    ) -> int:
        return self.model.objects.bulk_update(
            objs=instances, fields=fields, batch_size=batch_size
        )

class AbstractRepository(
    Generic[TModel],
    AbstractFetchRepository[TModel],
    AbstractEditRepository[TModel],
    ABC,
):
    ...