import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";
import UserList from "./Components/UserList";
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import {BrowserRouter, Link, Navigate, Route, Routes} from "react-router-dom";
import ProjectList from "./Components/ProjectList";
import TodoList from "./Components/TodoList";
import ProjectDetail from "./Components/ProjectDetail";
import LoginForm from "./Components/LoginForm";


class App extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({'token': token}, this.get_data)
    }

    get_data() {
        let headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
            const users = response.data.results
            this.setState({'users': users})
        }).catch(err => {
            console.log(err)
        })

        axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
            const projects = response.data.results
            this.setState({'projects': projects})
        }).catch(err => {
            console.log(err)
        })

        axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
            const todos = response.data.results
            this.setState({'todos': todos})
        }).catch(err => {
            console.log(err)
        })
    }

    get_headers() {
        if (this.is_authenticated()) {
            return {
                'Authorization': `Token ${this.state.token}`
            }
        }
        return {}
    }

    is_authenticated() {
        return !!this.state.token
    }


    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {'username': login, 'password': password})
            .then(response => {
                const token = response.data.token
                console.log(`sending post to api-token-auth from get_token using login:${login}, password:${password}, and got token: ${token}`)
                localStorage.setItem('token', token)
                console.log(`token saved to localStorage`)

                this.setState({'token': token}, this.get_data)
            }).catch(error => {
            console.log(error)
        })
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        })
    }


    render() {
        return (
            <div>
                {/*<HashRouter>*/}
                <BrowserRouter>
                    {/*<Header/>*/}
                    <ul>
                        <li><Link to={'/users'}>Users</Link></li>
                        <li><Link to={'/projects'}>Projects</Link></li>
                        <li><Link to={'/todos'}>Todos</Link></li>
                        <li>{this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to="/login">Login</Link>}</li>
                    </ul>

                    <Routes>
                        <Route exact path='/' element={<h1>Hope page</h1>}/>
                        {/*<Route exact path='/users' element={<Navigate to="/"/>}/>*/}
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/project/:id' element={<ProjectDetail projects={this.state.projects}/>}/>
                        <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>
                        <Route exact path='/login' element={<LoginForm form_get_token={(login, password) => this.get_token(login, password)}/>}/>

                        <Route path='*' element={<main><p>nothing here, 404, page not found, get out of here</p></main>}/>
                    </Routes>

                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }

}

export default App;
