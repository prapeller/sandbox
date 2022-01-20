const TodoItem = ({todo, deactivateTodo}) => {
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.creator}</td>
            <td>{todo.text}</td>
            <td>{todo.project}</td>
            <td>{`${todo.is_active}`}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td><button onClick={()=>deactivateTodo(todo.id)} type={'button'}>Deactivate</button></td>
        </tr>
    )
}

const TodoList = ({todos, deactivateTodo}) => {
    return (
        <table>
            <th>Id</th>
            <th>Creator ID</th>
            <th>Text</th>
            <th>Project ID</th>
            <th>Is active</th>
            <th>Created</th>
            <th>Updated</th>
            {todos.map((t) => <TodoItem todo={t} deactivateTodo={deactivateTodo}/>)}
        </table>
    )
}

export default TodoList;