import logo from './logo.svg';
import './App.css';
import React from "react";
import {HashRouter, BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import AuthorList from "./components/AuthorList";
import BookList from "./components/BookList";
import AuthorBooks from "./components/AuthorBooks";
import Footer from "./components/Footer";
import Header from "./components/Header";
import axios from "axios";


class App extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'authors': [],
            'books': []

        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/modelviewset_authors/').then(response => {
            const authors = response.data
            this.setState({
                'authors': authors
            })
        }).catch(error => {
            console.log(error)
        })

        axios.get('http://127.0.0.1:8000/api/modelviewset_books/').then(response => {
            const books = response.data
            this.setState({
                'books': books
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
                        <Route exact path='/' element={<h1>hello</h1>}/>
                        <Route exact path='/authorss' element={<Navigate to="/"/>}/>
                        <Route exact path='/authors' element={<AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' element={<BookList books={this.state.books}/>}/>
                        <Route exact path='/authorbooks/:id' element={<AuthorBooks books={this.state.books}/>}/>
                        <Route path='*' element={<main><p>nothing here, 404, page not found, get out of here</p></main>}/>
                    </Routes>

                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}

// function App()
//
//     {
//     return (
//         <div className="App">
//             <header className="App-header">
//                 <img src={logo} className="App-logo" alt="logo"/>
//                 <p>
//                     Edit <code>src/App.js</code> and save to reload.
//                 </p>
//                 <a
//                     className="App-link"
//                     href="https://reactjs.org"
//                     target="_blank"
//                     rel="noopener noreferrer"
//                 >
//                     Learn React
//                 </a>
//             </header>
//         </div>
//     );
// }

export default App;
