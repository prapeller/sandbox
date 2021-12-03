user_seconds = int(input('enter seconds number > '))

hours = f'{user_seconds // 3600:02d}'
minutes = f'{((user_seconds % 3600) // 60):02d}'
seconds = f'{((user_seconds % 3600) % 60):02d}'

print(f'{hours}:{minutes}:{seconds}')
