import os
from fastapi import Depends, APIRouter
from jwtdown_fastapi.authentication import Authenticator, Token
from queries.accounts import AccountRepo, AccountOut, AccountOutWithPassword


class MyAuthenticator(Authenticator):
    @property  # override router property so I can set my own tags
    def router(self):
        if self._router is None:
            router = APIRouter(tags=["Authentication"])
            router.post(f"/{self.path}", response_model=Token)(self.login)
            router.delete(f"/{self.path}", response_model=bool)(self.logout)
            self._router = router
        return self._router

    async def get_account_data(
        self,
        email: str,
        accounts: AccountRepo,
    ):
        # Use your repo to get the account based on the
        # username (which could be an email)
        return accounts.get(email)

    def get_account_getter(
        self,
        accounts: AccountRepo = Depends(),
    ):
        # Return the accounts. That's it.
        return accounts

    def get_hashed_password(self, account: AccountOutWithPassword):
        # Return the encrypted password value from your
        # account object
        return account.hashed_password

    def get_account_data_for_cookie(self, account: AccountOut):
        # Return the username and the data for the cookie.
        # You must return TWO values from this method.
        return account.email, AccountOut(**account.dict())


authenticator = MyAuthenticator(os.environ["SIGNING_KEY"])
