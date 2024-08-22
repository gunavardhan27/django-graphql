import graphene
from .mutations import Mutation
from .models import Post
from .types import PostType
from .decorators import login_required
class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    @login_required
    def resolve_posts(self,info):
        return Post.objects.all()

schema = graphene.Schema(mutation=Mutation,query=Query)