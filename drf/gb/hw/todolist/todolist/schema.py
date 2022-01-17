import graphene
import graphene_django

from todo.models import Project, Todo
from users.models import User


class UserType(graphene_django.DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, username=None):
        user = User.objects.get(pk=id)
        if username:
            user.username = username
            user.save()
        return UserMutation(user=user)


class TodoType(graphene_django.DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(graphene_django.DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))

    all_todos = graphene.List(TodoType)
    todo_by_creator_username = graphene.Field(TodoType, username=graphene.String(required=True))

    all_projects = graphene.List(ProjectType)
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    projects_by_user_username = graphene.List(ProjectType, username=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_user_by_username(root, info, username):
        return User.objects.get(username=username)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_todo_by_creator_username(root, info, username):
        return Todo.objects.get(creator__username=username)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_projects_by_user_username(root, info, username):
        user = User.objects.get(username=username)
        return Project.objects.all().filter(users__in=[user])


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
