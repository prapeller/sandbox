const TodoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.is_active}</td>
            <td>{todo.creator_id}</td>
            <td>{todo.project_id}</td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <th>Id</th>
            <th>Text</th>
            <th>Created at</th>
            <th>Updated at</th>
            <th>Is active</th>
            <th>Creator ID</th>
            <th>Project ID</th>
            {todos.map((t) => <TodoItem todo={t}/>)}
        </table>
    )
}

export default TodoList;