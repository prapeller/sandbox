import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";
import UserList from "./Components/UserList";
import Header from "./Components/Header";
import Footer from "./Components/Footer";


class App extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'users': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            const users = response.data
            this.setState({
                'users': users
            })
        }).catch(error => {
            console.log(error)
        })
    }

    render () {
        return(
            <div>
                <Header/>
                <UserList users={this.state.users}/>
                <Footer/>
            </div>
        )
    }

}

export default App;
