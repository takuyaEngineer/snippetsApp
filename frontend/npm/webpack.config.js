// Generated using webpack-cli https://github.com/webpack/webpack-cli

const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const isProduction = process.env.NODE_ENV == 'production';

const stylesHandler = isProduction ? MiniCssExtractPlugin.loader : 'style-loader';


const config = {
    entry: '../js/index.js',
    mode: 'production',
    output: {
        path: path.resolve(__dirname, '../../static/webpack'),
        filename: "bundle.js"
    },
    resolve: {
        modules: [path.resolve(__dirname, "../npm/node_modules")],
    },
    // devServer: {
    //     open: true,
    //     host: 'localhost',
    // },
    plugins: [
        // Add your plugins here
        // Learn more about plugins from https://webpack.js.org/configuration/plugins/
    ],
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/i,
                loader: 'babel-loader',
            },
            {
                test: /\.css$/i,
                use: [stylesHandler, 'css-loader'],
            },
            {
                test: /\.s[ac]ss$/i,
                use: [stylesHandler, 'css-loader', 'sass-loader'],
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/i,
                type: 'asset',
            },

            // Add your rules for custom modules here
            // Learn more about loaders from https://webpack.js.org/loaders/
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "style.css"
        })
    ]
};

// module.exports = () => {
//     if (isProduction) {
//         config.mode = 'production';

//         config.plugins.push(new MiniCssExtractPlugin());


//     } else {
//         config.mode = 'development';
//     }
//     return config;
// };
module.exports = [
    config
]