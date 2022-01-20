import React from 'react'

class TodoForm extends React.Component {
    constructor(prop) {
        super(prop);
        this.state = {
            'text': '',
            'project': '',
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleProjectChange(event) {
        // let project = ''
        // if (!event.target.selectedOptions) {
        //     this.state['project'] = ''
        //     return
        // }
        // for (let i = 0; i < event.target.selectedOptions.length; i++) {
        // console.log(event.target.selectedOptions.item(i).value)
        // }
        let project = event.target.value
        this.setState({
            'project': project
        })
    }

    handleSubmit(event) {
        console.log(`text:${this.state.text} project:${this.state.project}`)
        this.props.createTodo(this.state.text, this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name={"text"} placeholder={"text"} value={this.state.text}
                       onChange={(event) => this.handleChange(event)}/>

                <select
                    name={"projects"}
                    onChange={(event) => this.handleProjectChange(event)}>
                    {this.props.projects.map((p) => <option value={p.id}>{p.name}</option>)}
                </select>
                <input type="submit" value={"Create"}/>
            </form>
        )
    }
}

export default TodoForm;