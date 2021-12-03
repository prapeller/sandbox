import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Author";
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/').then(
            response => {
                const resp_authors = response.data
                this.setState({'authors': resp_authors})
            }
        ).catch(error => console.log(error))

        // const testAuthors = [
        //     {'first_name': 'Alexander', 'last_name': 'Pupkin', 'birthday_year': 2029},
        //     {'first_name': 'Lev', 'last_name': 'Tolstiy', 'birthday_year': 3029},
        // ]


    }

    render() {
        return (
            <div>
                <AuthorList authors={this.state.authors}/>
            </div>
        )
    }
}

export default App;
