import Todo from "./components/Todo";
import {Route, Switch} from "react-router-dom";
import AllMeetupPage from "./pages/AllMeetups";
import NewMeetupPage from "./pages/NewMeetup";
import FavoritesPage from "./pages/Favorites";
// import MainNavigation from "./components/layout/MainNavigation";
import Layout from "./components/layout/Layout";

function App() {

    return (
        <Layout>
            <Switch>
                <Route path={'/'} exact>
                    <AllMeetupPage/>
                </Route>
                <Route path={'/new-meetup'}>
                    <NewMeetupPage/>
                </Route>
                <Route path={'/favorites'}>
                    <FavoritesPage/>
                </Route>
            </Switch>
        </Layout>
    );
}

export default App;
