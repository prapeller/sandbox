import React from 'react'

class ProjectForm extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'name': '',
            'link': '',
            'users': []
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUsersChange(event) {
        let users = []
        if (!event.target.selectedOptions) {
            this.state['users'] = []
            return
        }
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            // console.log(event.target.selectedOptions.item(i).value)
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
        console.log(`name:${this.state.name} link:${this.state.link} users:${this.state.users}`)
        this.props.createProject(this.state.name, this.state.link, this.state.users)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name={"name"} placeholder={"name"} value={this.state.name}
                       onChange={(event) => this.handleChange(event)}/>
                <input type="text" name={"link"} placeholder={"link"} value={this.state.link}
                       onChange={(event) => this.handleChange(event)}/>

                <select multiple name={"users"}
                        onChange={(event) => this.handleUsersChange(event)}>
                    {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
                </select>
                <input type="submit" value={"Create"}/>
            </form>
        )
    }
}

export default ProjectForm;