from typing import Union, List

from ..asset import Asset
from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient
from ..utils import convert_assets_to_horizon_param


class AccountsCallBuilder(BaseCallBuilder):
    """ Creates a new :class:`AccountsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.accounts`.

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "accounts"

    def account_id(self, account_id: str) -> "AccountsCallBuilder":
        """Returns information and links relating to a single account.
        The balances section in the returned JSON will also list all the trust lines this account has set up.

        See `Account Details <https://www.stellar.org/developers/horizon/reference/endpoints/accounts-single.html>`_

        :param account_id: account id, for example: `GDGQVOKHW4VEJRU2TETD6DBRKEO5ERCNF353LW5WBFW3JJWQ2BRQ6KDD`
        :return: current AccountCallBuilder instance
        """
        self.endpoint = "accounts/{account_id}".format(account_id=account_id)
        return self

    def signer(self, signer: str) -> "AccountsCallBuilder":
        """Filtering accounts who have a given signer. The result is a list of accounts.

        See `Account Details <https://www.stellar.org/developers/horizon/reference/endpoints/accounts-single.html>`_

        :param signer: signer's account id, for example: `GDGQVOKHW4VEJRU2TETD6DBRKEO5ERCNF353LW5WBFW3JJWQ2BRQ6KDD`
        :return: current AccountCallBuilder instance
        """
        self._add_query_param("signer", signer)
        return self

    def asset(self, asset: Asset) -> "AccountsCallBuilder":
        """Filtering accounts who have a trustline to an asset. The result is a list of accounts.

        See `Account Details <https://www.stellar.org/developers/horizon/reference/endpoints/accounts-single.html>`_

        :param assets: a list of one or more Assets
        :return: current AccountCallBuilder instance
        """
        assets_param = convert_assets_to_horizon_param([asset])
        self._add_query_param("asset", assets_param)
        return self
