import {Link} from "react-router-dom";

const Header = () => {
    return (
        <ul>
            <li><Link to={'/users'}>Users</Link></li>
            <li><Link to={'/projects'}>Projects</Link></li>
            <li><Link to={'/todos'}>Todos</Link></li>
        </ul>
    )
}

export default Header