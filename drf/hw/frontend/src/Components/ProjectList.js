import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/project-users/${project.id}`}>{project.name}</Link></td>
            <td>{project.link}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Id</th>
            <th>Name</th>
            <th>Link</th>
            {projects.map((p) => <ProjectItem project={p}/>)}
        </table>
    )
}

export default ProjectList;