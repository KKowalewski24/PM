const User = require('../models/user');
const _ = require('underscore');
const Request = require("request");

exports.getAll = (req, res) => {
    User.getAll().then(
        function(allUsers) {
            console.log(allUsers);
            res.json(allUsers);
        }
    );
};

exports.getById = (req, res) => {
    User.getById(req.params.id).then(
        function(user) {
            res.json(user);
        }
    );
};

// store works as follows:
// 1. try to add new user to the database
// 2. if the operation is correct, try to send email
exports.store = (req, res) => {
    const newUser = User.create({
        'email': req.body.email,
        'name': req.body.name,
        'surname': req.body.surname,
        'birthdate': new Date(req.body.birthdate),
        'gender': req.body.gender
    }).then(function(data) {
        Request.post({
            "headers": { "content-type": "application/json" },
            "url": "http://"+ process.env.EMAIL_SERVICE_HOST +":8083/emails",
            "body": JSON.stringify({
                "email": newUser.email
            })
        }, (error, response, body) => {
            if(error) {
                return console.dir(error);
            }
            res.json({
                'status':'saved and email delivered!',
                'user': data,
            });
        });

        
    });
};

exports.updateById = (req, res) => {
    // Please note the API change!
    User.update(req.body.user).then(
        function(user) {
            res.json(user);
        }
    )    
}