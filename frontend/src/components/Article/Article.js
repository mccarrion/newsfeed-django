import React from 'react';

class Article extends React.Component {
  componentWillMount() {

  }

  render() {
    return (
      <div className="display-article">
        <div className="container">
          <div className="col-md-8 offset-md-2">
            <h1>{this.props.article.title}</h1>
            <img className="img-fluid" src="{this.props.image.url}" />
            <h3>{this.props.article.subtitle}</h3>
            <b>By {this.props.article.author}</b>
            <p>{this.props.article.date}</p>
            <p>{this.props.article.body|safe|linebreaks}</p>
          </div>
        </div>
      </div>
    );
  }
}