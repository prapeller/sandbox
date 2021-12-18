import {Link} from 'react-router-dom'

const ProjectItem = ({project}) => {
    return(
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/project/${project.id}`}>{project.name}</Link></td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>Id</th>
            <th>Name</th>
            {projects.map((p) => <ProjectItem project={p}/>)}
        </table>
    )
}

export default ProjectList;