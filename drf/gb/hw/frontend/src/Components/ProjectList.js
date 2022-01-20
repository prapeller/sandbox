import {Link} from 'react-router-dom'

const ProjectItem = ({project, deleteProject}) => {
    return(
        <tr>
            <td>{project.id}</td>
            <td><Link to={`/project/${project.id}`}>{project.name}</Link></td>
            <td><button onClick={()=>deleteProject(project.id)} type={'button'}>Delete</button></td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <table>
            <th>Id</th>
            <th>Name</th>
            {projects.map((p) => <ProjectItem project={p} deleteProject={deleteProject}/>)}
        </table>
    )
}

export default ProjectList;