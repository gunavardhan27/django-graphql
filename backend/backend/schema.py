import graphene

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

#after creating an account or registering we get a registratn token to the emailbackend we have use that token to verify the user
#tokenauth used to login and also generate a jsonwebtoken which in turn can be used to delete or update our accounts
class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
    
class Mutation(AuthMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query,mutation=Mutation)