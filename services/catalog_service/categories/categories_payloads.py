from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class NestedItem:
    id: Optional[int] = None
    sortIndex: Optional[int] = None


@dataclass
class CategoriesPayloads:
    categoryIds: Optional[list] = None
    categoryId: Optional[int] = None
    id: Optional[int] = None
    correlationId: Optional[str] = None
    parentId: Optional[int] = None
    caption: Optional[str] = None
    status: Optional[int] = None
    isLastNode: Optional[bool] = None
    sortIndex: Optional[int] = None
    description: Optional[str] = None
    shouldChooseBrand: Optional[bool] = None
    isBrandMandatory: Optional[bool] = None
    shouldChooseModel: Optional[bool] = None
    isModelMandatory: Optional[bool] = None
    shouldFillInstallation: Optional[bool] = None
    isInstallationMandatory: Optional[bool] = None
    shouldFillProductReturnDetails: Optional[bool] = None
    isProductReturnDetailsMandatory: Optional[bool] = None
    shouldFillCondition: Optional[bool] = None
    isConditionMandatory: Optional[bool] = None
    hasInstallment: Optional[bool] = None
    ageContentRestriction: Optional[bool] = None
    notSearchableRestriction: Optional[bool] = None
    iconFileName: Optional[str] = None
    shippingPackageSizeId: Optional[int] = None
    featureId: Optional[int] = None
    isC2C: Optional[bool] = None
    isMandatory: Optional[bool] = None
    previousItem: NestedItem = None
    item: NestedItem = None

    @staticmethod
    def post_check_node_categories(category_ids: list):
        payload = CategoriesPayloads(
            categoryIds=category_ids
        )
        return payload
