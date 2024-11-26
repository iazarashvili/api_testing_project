from dataclasses import dataclass
from typing import Optional, List


@dataclass
class PreferredCategory:
    categoryId: Optional[int] = None
    categoryCaption: Optional[str] = None


@dataclass
class UpdatePhysical:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    personalNumber: Optional[str] = None
    birthDate: Optional[str] = None
    gender: Optional[int] = None
    isPetOwner: Optional[bool] = None
    preferredCategories: Optional[List[PreferredCategory]] = None


@dataclass
class ChangeEmail:
    id: Optional[int] = None
    email: Optional[str] = None


@dataclass
class ConfirmEmail:
    id: Optional[int] = None
    otp: Optional[str] = None


@dataclass
class AddPhoneNumber:
    phoneNumber: Optional[str] = None
    default: Optional[bool] = None
    otp: Optional[str] = None


@dataclass
class SendVerification:
    phoneNumber: Optional[str] = None


@dataclass
class WorkSchedule:
    fromHours: Optional[str] = None
    toHours: Optional[str] = None
    weekDay: Optional[int] = None


@dataclass
class Address:
    addressId: Optional[int] = None
    city: Optional[dict] = None
    street: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    phoneNumber: Optional[str] = None
    contactPerson: Optional[str] = None
    workSchedule: Optional[List[WorkSchedule]] = None
    isBasicAddress: Optional[bool] = None
    emails: Optional[List[str]] = None


@dataclass
class LegalCreate:
    email: Optional[str] = None
    phone: Optional[str] = None
    emailConfirmed: Optional[bool] = None
    phoneConfirmed: Optional[bool] = None
    contactPhoneNumber: Optional[str] = None
    avatarGuid: Optional[str] = None
    coverPhoto: Optional[str] = None
    identityNumber: Optional[str] = None
    juridicalTitle: Optional[str] = None
    commercialTitle: Optional[str] = None
    agreementGuid: Optional[str] = None
    externalId: Optional[str] = None
    address: Optional[Address] = None
    agreementType: Optional[int] = None
    guaranteeFileName: Optional[str] = None
    commercialTitleEng: Optional[str] = None
    commercialTitleKa: Optional[str] = None
    deliveryTime: Optional[int] = None
    priority: Optional[int] = None


@dataclass
class Manager:
    id: Optional[int] = None
    managerId: Optional[str] = None


@dataclass
class AddManager:
    customerId: Optional[str] = None
    managers: Optional[List[Manager]] = None


@dataclass
class AddAddress:
    customerId: Optional[str] = None
    address: Optional[List[Address]] = None


@dataclass
class UpdateAddress:
    customerId: Optional[str] = None
    address: Optional[List[Address]] = None


@dataclass
class UpdateLegal:
    id: Optional[int] = None
    identityNumber: Optional[str] = None
    juridicalTitle: Optional[str] = None
    commercialTitle: Optional[str] = None
    agreementGuid: Optional[str] = None
    avatarGuid: Optional[str] = None
    coverPhoto: Optional[str] = None
    externalId: Optional[str] = None
    agreementType: Optional[int] = None
    commercialTitleEng: Optional[str] = None
    commercialTitleKa: Optional[str] = None
    phoneNumber: Optional[str] = None
    contactPhoneNumber: Optional[str] = None
    email: Optional[str] = None
    priority: Optional[int] = None


@dataclass
class AddSizeGuide:
    categoryId: Optional[List[int]] = None
    customerId: Optional[str] = None
    photoName: Optional[str] = None


@dataclass
class ChangeShippingOptions:
    merchantId: Optional[str] = None
    shippingOptions: Optional[List[int]] = None


@dataclass
class CustomerProductView:
    productId: Optional[int] = None
    darkStoreId: Optional[int] = None


@dataclass
class IsOptedForAds:
    isOptedForAds: Optional[bool] = None


@dataclass
class AddShippingAddress:
    customerId: Optional[str] = None
    locationId: Optional[int] = None
    location: Optional[str] = None
    address: Optional[str] = None
    addressAdditionalInfo: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    isDefault: Optional[bool] = None
    userType: Optional[int] = None


@dataclass
class ChangeDefaultShipping:
    customerId: Optional[str] = None
    id: Optional[int] = None
    isDefault: Optional[bool] = None
    userType: Optional[int] = None


@dataclass
class EditShippingAddress:
    customerId: Optional[str] = None
    id: Optional[int] = None
    locationId: Optional[int] = None
    location: Optional[str] = None
    address: Optional[str] = None
    addressAdditionalInfo: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    isDefault: Optional[bool] = None
    userType: Optional[int] = None


@dataclass
class ChangeBasicAddress:
    customerId: Optional[str] = None
    addressId: Optional[int] = None


@dataclass
class ChangeDashboardStatus:
    id: Optional[int] = None
    hasDashboard: Optional[bool] = None


@dataclass
class ChangeMerchantHasUserInformation:
    merchantId: Optional[str] = None
    hasUserInformationView: Optional[bool] = None


@dataclass
class Guarantee:
    userId: Optional[str] = None
    fileName: Optional[str] = None


@dataclass
class DeliveryTime:
    merchantId: Optional[str] = None
    deliveryTime: Optional[int] = None


@dataclass
class RepresentedUser:
    representedUserId: Optional[str] = None
    userType: Optional[int] = None


@dataclass
class UpdateRepresentativeRelationships:
    representativeId: Optional[str] = None
    representedUserIds: Optional[List[RepresentedUser]] = None


@dataclass
class AddRepresentativeToMerchant:
    representativeId: Optional[str] = None
    merchantId: Optional[str] = None


@dataclass
class RemoveRepresentativeToMerchant:
    representativeId: Optional[str] = None
    merchantId: Optional[str] = None


@dataclass
class UpdateRepresentativeRelationshipsByEntityType:
    representativeId: Optional[str] = None
    type: Optional[int] = None
    representedUserIds: Optional[List[str]] = None


@dataclass
class WorkingHourData:
    isAvailable: Optional[bool] = None
    weekDay: Optional[int] = None


@dataclass
class WorkingHours:
    userId: Optional[str] = None
    workingHours: Optional[List[WorkingHourData]] = None


# Example usage:
"""
data = {
  "userIds": ["user123", "user456", "user789"]
}
user_ids_info = UserIds(**data)
"""


@dataclass
class GetCustomerAddresses:
    userIds: Optional[List[str]] = None
