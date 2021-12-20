import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";
import UserList from "./Components/UserList";
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import ProjectList from "./Components/ProjectList";
import TodoList from "./Components/TodoList";
import ProjectDetail from "./Components/ProjectDetail";


class App extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            const users = response.data.results
            console.log(users)
            this.setState({
                'users': users
            })
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
            const projects = response.data.results
            this.setState({
                'projects': projects
            })
        }).catch(error => {
            console.log(error)
        })
        axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
            const todos = response.data.results
            this.setState({
                'todos': todos
            })
        }).catch(error => {
            console.log(error)
        })
    }

    render() {
        return (
            <div>
                {/*<HashRouter>*/}
                <BrowserRouter>
                    <Header/>

                    <Routes>
                        <Route exact path='/' element={<h1>Hope page</h1>}/>
                        {/*<Route exact path='/users' element={<Navigate to="/"/>}/>*/}
                        <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/project/:id' element={<ProjectDetail projects={this.state.projects}/>}/>
                        <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>

                        <Route path='*' element={<main><p>nothing here, 404, page not found, get out of here</p></main>}/>
                    </Routes>

                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }

}

export default App;
