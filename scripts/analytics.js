const incrementVisitCounter = () => {
	const foundVisits = window.localStorage.getItem('_mphVisits');
	const visits = (foundVisits && parseInt(foundVisits))++ || 1;
	window.localStorage.setItem('_mphVisits', visits);
	return visits;
}
