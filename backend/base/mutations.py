
import graphene
from .models import User,Post
from .types import PostType
from .decorators import login_required,allowed_roles
class CreatePostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
    post = graphene.Field(PostType)
    success = graphene.Boolean()
    
    @login_required
    @allowed_roles(allowed_users=['Admin'])
    def mutate(self,info,title,description):
        data = Post.objects.filter(id=info.context.user.id,title=title)
        if not data:
            post = Post.objects.create(owner=info.context.user,title=title,description=description)
        else:
            raise Exception('post already exists with similar name')
        return CreatePostMutation(post=post,success=True)
            
        
class Mutation(graphene.ObjectType):
    add_post = CreatePostMutation.Field()