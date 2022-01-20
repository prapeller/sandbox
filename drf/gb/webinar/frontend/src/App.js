import logo from './logo.svg';
import './App.css';
import React from "react";
import {HashRouter, BrowserRouter, Routes, Route, Navigate, Link} from "react-router-dom";
import AuthorList from "./components/AuthorList";
import BookList from "./components/BookList";
import AuthorBooks from "./components/AuthorBooks";
import Footer from "./components/Footer";
import Header from "./components/Header";
import axios from "axios";
import LoginForm from "./components/LoginForm";
import BookForm from "./components/BookForm";


export class App extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'authors': [],
            'books': [],
            'token': '',
        }
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({'token': token}, this.get_data)
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

    get_headers() {
        if (this.is_auth()) {
            return {
                'Authorization': `Token ${this.state.token}`
            }
        }
        return {}
    }


    get_data() {
        let headers = this.get_headers()
        axios
            .get('http://127.0.0.1:8000/api/modelviewset_authors/', {headers})
            .then(response => {
                const authors = response.data
                this.setState({
                    'authors': authors
                })
            }).catch(error => {
            console.log(error)
        })

        axios
            .get('http://127.0.0.1:8000/api/modelviewset_books/', {headers})
            .then(response => {
                const books = response.data
                this.setState({
                    'books': books
                })
            }).catch(error => {
            console.log(error)
        })


    }

    deleteBook(id) {
        let headers = this.get_headers()
        axios
            .delete(`http://127.0.0.1:8000/api/modelviewset_books/${id}`, {headers})
            .then(response => {
                const authors = response.data
                this.setState({
                    'books': this.state.books.filter((book) => book.id != id)
                })
            }).catch(error => {
            console.log(error)
        })
    }

    createBook(name, authors) {
        let headers = this.get_headers()
        axios
            .post('http://127.0.0.1:8000/api/modelviewset_books/', {'name': name, 'authors': authors}, {headers})
            .then(response => {
                this.get_data()
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        return (
            <div>
                {/*<HashRouter>*/}
                <BrowserRouter>
                    {/*<Header/>*/}
                    <ul>
                        <li><Link to="/authors">Authors</Link></li>
                        <li><Link to="/books">Books</Link></li>
                        <li><Link to="/books/create">Create Book</Link></li>
                        <li>{this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to="/login">Login</Link>}</li>
                    </ul>

                    <Routes>
                        <Route exact path='/' element={<h1>hello</h1>}/>
                        <Route exact path='/authorss' element={<Navigate to="/"/>}/>
                        <Route exact path='/authors' element={<AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' element={<BookList books={this.state.books} deleteBook={(id) => this.deleteBook(id)}/>}/>
                        <Route exact path='/books/create' element={<BookForm authors={this.state.authors} createBook={(name, authors) => this.createBook(name, authors)}/>}/>}/>
                        <Route exact path='/authorbooks/:id' element={<AuthorBooks books={this.state.books}/>}/>
                        <Route exact path='/login' element={<LoginForm form_get_token={(login, password) => this.get_token(login, password)}/>}/>
                        <Route path='*' element={<main><p>nothing here, 404, page not found, get out of here</p></main>}/>
                    </Routes>

                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }

    is_auth() {
        return !!this.state.token
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({
            'authors': [],
            'books': [],
            'token': '',
        })
    }
}


export default App;
