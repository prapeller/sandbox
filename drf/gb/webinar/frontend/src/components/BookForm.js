import React from 'react'

class BookForm extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'name': '',
            'authors': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleAuthorsChange(event) {
        let authors = []
        if (!event.target.selectedOptions) {
            this.state['authors'] = []
            return
        }
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            authors.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'authors': authors
        })
    }

    handleSubmit(event) {
        // console.log(`name:${this.state.name} pass:${this.state.authors}`)
        this.props.createBook(this.state.name, this.state.authors)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name={"name"} placeholder={"name"} value={this.state.name}
                       onChange={(event) => this.handleChange(event)}/>

                <select multiple name={"authors"} placeholder={"authors"}
                        onChange={(event) => this.handleAuthorsChange(event)}>
                    {this.props.authors.map((a) => <option value={a.id}>{a.first_name} {a.last_name}</option>)}
                </select>
                <input type="submit" value={"Create"}/>
            </form>
        )
    }
}

export default BookForm;