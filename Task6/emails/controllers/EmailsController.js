exports.send = (req, res) => {
    const address = req.body.email;
    setTimeout(function(address) {
        res.json({
            'status':'delivered',
            'user': req.body.email,
        });
        console.log(`Email sent.`);
    },5000);    
};