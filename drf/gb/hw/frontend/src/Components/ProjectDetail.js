import {Link, useParams} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/project/${project.id}`}>{project.name}</Link></td>
            <td>{project.link}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectDetail = ({projects}) => {
    let {id} = useParams();
    let p = projects.filter((p) => p.id === (parseInt(id)))[0]

    return (
        <table>
            <th>Id</th>
            <th>Name</th>
            <th>Link</th>
            <th>Users</th>
            {<ProjectItem project={p}/>}
            {/*<tr>*/}
            {/*    <td>{p.id}</td>*/}
            {/*    <td>{p.name}</td>*/}
            {/*    <td>{p.link}</td>*/}
            {/*    <td>{p.users}</td>*/}
            {/*</tr>*/}
        </table>
    )
}

export default ProjectDetail;