const amqp = require('amqplib/callback_api');

exports.publish_email = () => {
    const connectionString = 'amqp://' + process.env.BROKER_HOST + ':' + process.env.BROKER_PORT;

    amqp.connect(connectionString, function (error0, connection) {
        if (error0) {
            throw error0;
        }

        connection.createChannel(function (error1, channel) {
            if (error1) {
                throw error1;
            }

            const exchange = 'logs';
            const msg = process.argv.slice(2).join(' ') || 'Hello World!';

            channel.assertExchange(exchange, 'fanout', {
                durable: false
            });

            channel.publish(exchange, '', Buffer.from(msg));
            console.log(" [x] Sent %s", msg);
        });

        setTimeout(function () {
            connection.close();
            process.exit(0);
        }, 500);
    });
};
