from services.basket_service.basket.basket_api import BasketApi
from services.identity_service.roles.roles_api import RolesApi
from services.basket_service.wish_list.wish_list_api import WishListApi
from services.basket_service.admin_basket.admin_basket_api import AdminBasketApi
from services.ordering_service.orders.orders_api import OrdersApi
from services.payment_service.payment.payment_api import PaymentApi
from services.ordering_service.order_reservation.order_reservation_api import OrderReservationApi
from services.mercury_services.search.search_api import SearchApi
from services.mercury_services.products.products_api import ProductsApi
from services.delivery_integration_service.izi_box_integration.izi_box_integration_api import IziBoxIntegrationApi
from services.mercury_services.filters.filters_api import FiltersApi
from services.mercury_services.categories.categoryes_api import MercuryCategoriesApi
from services.catalog_service.advertisements.advertisements_api import AdvertisementsApi
from services.catalog_service.brands.brands_api import BrandApi
from services.catalog_service.date.date_api import DateApi
from services.catalog_service.feature_group.feature_group_api import FeatureGroupApi
from services.catalog_service.features_suggested_values.feature_suggested_values_api import FeatureSuggestedValuesApi
from services.catalog_service.feeds.feeds_api import FeedsApi
from services.catalog_service.categories.categories_api import CategoriesApi
from services.catalog_service.collector_hub.collector_hub_api import CollectorHubApi
from services.catalog_service.express.express_api import ExpressApi
from services.catalog_service.features.features_api import FeaturesApi
from services.catalog_service.integrations.integrations_api import IntegrationApi
from services.catalog_service.locations.locations_api import LocationApi
from services.catalog_service.manufacturer_countries.manufacturer_countries_api import ManufacturerCountriesApi
from services.catalog_service.merchants.merchants_api import MerchantApi
from services.catalog_service.mobile_categories.mobile_categories_api import MobileCategoriesApi
from services.catalog_service.model.model_api import ModelApi
from services.catalog_service.notification.notification_api import NotificationApi


class BaseApi:
    basket_api = BasketApi()
    identity_roles_api = RolesApi()
    basket_wish_list_api = WishListApi()
    basket_admin_basket_api = AdminBasketApi()
    ordering_orders_api = OrdersApi()
    payment_api = PaymentApi()
    ordering_order_reservation_api = OrderReservationApi()
    mercury_categories_api = MercuryCategoriesApi()
    mercury_search_api = SearchApi()
    mercury_products_api = ProductsApi()
    mercury_filters_api = FiltersApi()
    izi_integration_api = IziBoxIntegrationApi()
    catalog_advertisements_api = AdvertisementsApi()
    catalog_brands_api = BrandApi()
    catalog_data_api = DateApi()
    catalog_feature_group_api = FeatureGroupApi()
    catalog_feature_suggested_values_api = FeatureSuggestedValuesApi()
    catalog_feeds_api = FeedsApi()
    catalog_categories_api = CategoriesApi()
    catalog_collector_hub_api = CollectorHubApi()
    catalog_express_express_api = ExpressApi()
    catalog_features_api = FeaturesApi()
    catalog_integration_api = IntegrationApi()
    catalog_locations_api = LocationApi()
    catalog_manufacturer_countries_api = ManufacturerCountriesApi()
    catalog_merchants_api = MerchantApi()
    catalog_mobile_categories_api = MobileCategoriesApi()
    catalog_model_api = ModelApi()
    catalog_notification_api = NotificationApi()
