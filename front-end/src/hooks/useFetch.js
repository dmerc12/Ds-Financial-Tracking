export const useFetch = () => {

    const fetchData = async (url, requestMethod, requestBody) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000${url}`, {
                method: requestMethod,
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(requestBody)
            });

            const data = await response.json();

            return {
                data: data,
                responseStatus: response.status
            }
        } catch (error) {
            throw new Error("Failed to fetch")
        }
    };

    return { fetchData };
};
