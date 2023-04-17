import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';

import { useNavigate } from "react-router-dom";

import { isTokenValid } from "./helpers/utils";
import { Logout } from '@mui/icons-material';

const pages = ['Shared With Me', 'Share Files', 'Share History'];
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];
const authSettings = ['Sign In', 'Sign Up'];

export default function Navbar() {
  const navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = (event) => {
    setAnchorElNav(null);
    console.log(event.target.innerText);
    switch (event.target.innerText) {
        case 'SHARED WITH ME':
            navigate('/shares');
            break;
        case 'SHARE FILES':
            navigate('/upload');
            break;
        case 'SHARE HISTORY':
            navigate('/history');
            break;
        default:
            break;
    }
  };

  const handleCloseAuthMenu = (event) => {
    setAnchorElUser(null);
    switch (event.target.innerText) {
        case 'SIGN IN':
            navigate('/sign-in');
            break;
        case 'SIGN UP':
            navigate('/sign-up');
            break;
        default:
            break;
    }
  };

  const handleLogout = () => {
    setAnchorElUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/sign-in');
  };


  return (
    <nav>
        <AppBar>
        <Container maxWidth="xl">
            <Toolbar disableGutters>
            <Typography
                variant="h6"
                noWrap
                component="a"
                href="/"
                sx={{
                mr: 2,
                display: { xs: 'none', md: 'flex' },
                // fontFamily: 'monospace',
                fontWeight: 700,
                letterSpacing: '.3rem',
                color: 'inherit',
                textDecoration: 'none',
                }}
            >
                WARPSHARE
            </Typography>

            <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
                <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleOpenNavMenu}
                color="inherit"
                >
                <MenuIcon />
                </IconButton>
                <Menu
                id="menu-appbar"
                anchorEl={anchorElNav}
                anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'left',
                }}
                keepMounted
                transformOrigin={{
                    vertical: 'top',
                    horizontal: 'left',
                }}
                open={Boolean(anchorElNav)}
                onClose={handleCloseNavMenu}
                sx={{
                    display: { xs: 'block', md: 'none' },
                }}
                >
                {pages.map((page) => (
                    <MenuItem key={page} onClick={handleCloseNavMenu}>
                    <Typography textAlign="center">{page}</Typography>
                    </MenuItem>
                ))}
                </Menu>
            </Box>
            <AdbIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
            <Typography
                variant="h5"
                noWrap
                component="a"
                href=""
                sx={{
                mr: 2,
                display: { xs: 'flex', md: 'none' },
                flexGrow: 1,
                fontFamily: 'monospace',
                fontWeight: 700,
                letterSpacing: '.3rem',
                color: 'inherit',
                textDecoration: 'none',
                }}
            >
                LOGO
            </Typography>
            <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                {pages.map((page) => (
                <Button
                    key={page}
                    onClick={handleCloseNavMenu}
                    sx={{ my: 2, color: 'white', display: 'block' }}
                >
                    {page}
                </Button>
                ))}
            </Box>

            <Box sx={{ flexGrow: 0, display: { xs: 'none', md: 'flex' }}}>
                {
                    !isTokenValid() ? 
                    (
                        authSettings.map((page) => (
                            <Button
                                key={page}
                                onClick={handleCloseAuthMenu}
                                sx={{ my: 2, color: 'white', display: 'block'}}
                            >
                                {page}
                            </Button>
                        ))
                    )
                    :
                    (
                        <Button
                            key='Logout'
                            onClick={handleLogout}
                            sx={{ my: 2, color: 'white', display: 'block' }}
                        >
                            Logout
                        </Button> 
                    )
                }
            </Box>
            </Toolbar>
        </Container>
        </AppBar>
    </nav>
  );
}