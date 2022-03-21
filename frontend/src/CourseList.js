import React, {Component} from "react";
import axios from "axios";


class CourseList extends Component {
    state = {
        courseList: []
    };

    componentDidMount() {
        this.getCourseList();
    }

    getCourseList() {
        axios
            .get('http://localhost:8000/api/courses')
            .then(res => {
                this.setState({courseList: res.data});
            })
            .catch(err => {
                console.log(err);
            });
    }

    render() {
        return (
              <div className="CourseList">
                {this.state.courseList.map(item =>
                  <div key={item.id}>
                    <h1>{item.name}</h1>
                    <span>
                      <strong>{item.course_id}</strong>
                    </span>
                  </div>
                )}
              </div>
        )
    }
}

export default CourseList;