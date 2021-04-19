const app = require('./app');

app.set('port', process.env.PORT || 8083);

const server = app.listen(app.get('port'), () => {
    console.log(`email service is listening on
    ${server.address().port}`);
});