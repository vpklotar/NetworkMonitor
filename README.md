# NetworkMonitor
[![Build Status](https://travis-ci.org/vpklotar/NetworkMonitor.png?branch=master)](https://travis-ci.org/vpklotar/NetworkMonitor) [![codecov.io Code Coverage](https://img.shields.io/codecov/c/github/vpklotar/NetworkMonitor.svg?maxAge=2592000)](https://codecov.io/gh/vpklotar/NetworkMonitor?branch=master) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/vpklotar/NetworkMonitor)

## What is NetworkMonitor?
NetworkMonitor (NM) is a network monitor written in Python to do monitoring of whatever you want. It works much like Nagios with the application itself not doing any monitoring. The application get it's monitoring data from calling scripts and interprets the data that is being output from the script.

## Why use NetworkMonitor?
NM is stil in its startup stage and at this stage it is easier to implement new funtionality.  NM also handles, what Nagios call Performance Data, better and automaticly handles it and creates the graphs.