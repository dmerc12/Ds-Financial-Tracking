import { dbConnection } from "./dbConnection";

const userTableSQL = '';
const values = [0]

const userTable = await dbConnection({ userTableSQL, values })