if(process.env.NODE_ENV !== "production") {
    require('dotenv').config();
}


const express = require('express');
const app = express();
const path = require('path');
const mongoose = require('mongoose');
const ejsMate = require('ejs-mate');
const ExpressError = require('./utils/ExpressError');
const methodOverride = require('method-override');
const campgroundRoutes = require('./routes/campgrounds'); 
const reviewRoutes = require('./routes/reviews'); 
const userRoutes = require('./routes/users'); 
const session = require('express-session');
const flash = require('connect-flash');
const passport = require('passport');
const LocalStrategy = require('passport-local');
const User = require('./models/user2');
const mongoSanitize = require('express-mongo-sanitize');
const helmet = require('helmet');
const dbURL = process.env.DB_URL || 'mongodb://localhost:27017/yelp-camp'
const MongoStore = require('connect-mongo');

// const dbURL = 'mongodb://localhost:27017/yelp-camp';
const secret = process.env.SECRET || 'thisshouldbeabettersecret';
mongoose.connect(dbURL)
    .then(()=> {
        console.log("MongoDB Connection Opened!");
    })
    .catch((error) =>{
        console.log("Oh no, database connection error!")
        console.log(error);
    })

app.engine('ejs', ejsMate);    
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));

app.use(express.urlencoded({extended: true}));
app.use(express.json());
app.use(methodOverride('_method'));

app.use(express.static('public'))
app.use(express.static(path.join(__dirname, '/public')))
app.use(mongoSanitize());

//create store
const store = MongoStore.create({
    mongoUrl: dbURL,
    touchAfter: 24 * 60 * 60, //how often you update
    crypto: {
        secret: secret
    }
});

store.on("error", function(e){
    console.log("Session Store Error")
})

const sessionConfig = {
    store,
    name: 'session',
    secret,
    resave: false,
    saveUninitialized: true,
    cookie: {
        httpOnly: true, //cookies only available through http not JS
        // secure: true, //this cookie will only work through https
        expires: Date.now() + 1000*60*60*24*7,
        maxAge: 1000*60*60*24*7,
    }
}
app.use(session(sessionConfig));
app.use(flash());

// app.use(helmet({
//     contentSecurityPolicy: false,
// }
// ));

const scriptSrcUrls = [
    "https://stackpath.bootstrapcdn.com/",
    "https://api.tiles.mapbox.com/",
    "https://api.mapbox.com/",
    "https://kit.fontawesome.com/",
    "https://cdnjs.cloudflare.com/",
    "https://cdn.jsdelivr.net/",
    "https://res.cloudinary.com/dcel4ewmg/"
];
const styleSrcUrls = [
    "https://kit-free.fontawesome.com/",
    "https://stackpath.bootstrapcdn.com/",
    "https://api.mapbox.com/",
    "https://api.tiles.mapbox.com/",
    "https://fonts.googleapis.com/",
    "https://use.fontawesome.com/",
    "https://cdn.jsdelivr.net/",
    "https://res.cloudinary.com/dcel4ewmg/"
];
const connectSrcUrls = [
    "https://*.tiles.mapbox.com",
    "https://api.mapbox.com",
    "https://events.mapbox.com",
    "https://res.cloudinary.com/dcel4ewmg/"
];
const fontSrcUrls = [ "https://res.cloudinary.com/dcel4ewmg/" ];

app.use(
    helmet.contentSecurityPolicy({
        directives : {
            defaultSrc : [],
            connectSrc : [ "'self'", ...connectSrcUrls ],
            scriptSrc  : [ "'unsafe-inline'", "'self'", ...scriptSrcUrls ],
            styleSrc   : [ "'self'", "'unsafe-inline'", ...styleSrcUrls ],
            workerSrc  : [ "'self'", "blob:" ],
            objectSrc  : [],
            imgSrc     : [
                "'self'",
                "blob:",
                "data:",
                "https://res.cloudinary.com/seanbyju/", //SHOULD MATCH YOUR CLOUDINARY ACCOUNT!
                "https://images.unsplash.com/",
                "https://res.cloudinary.com/dcel4ewmg/"
            ],
            fontSrc    : [ "'self'", ...fontSrcUrls ],
            mediaSrc   : [ "https://res.cloudinary.com/dv5vm4sqh/" ],
            childSrc   : [ "blob:" ]
        },
        crossOriginEmbedderPolicy: false
    })
);

app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));

passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

//for flash to work
app.use((req, res, next)=>{
    res.locals.currentUser = req.user;
    res.locals.success = req.flash('success');
    res.locals.error = req.flash('error');
    next();
})


app.use('/campgrounds', campgroundRoutes)
app.use('/campgrounds/:id/reviews', reviewRoutes)
app.use('/', userRoutes)

app.get('/', (req, res)=>{
    res.render('home')
})

app.all("*", (req, res, next)=>{
    next(new ExpressError('Page Not Found', 404))
})

app.use((err, req, res, next)=>{
    const {statusCode = 500} = err;
    if(!err.message){
        err.message = "Something went wrong!"
    }
    res.status(statusCode).render('error', {err});
})


app.listen(3000, () => {
    console.log('Serving on port 3000!')
})