<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  setup() {
    const tasks = ref([])
    const newTask = ref('')

    const apiId = 'aqnnns34m4' // Replace with your actual REST API ID
    const stage = 'dev' // Replace with your actual stage name

    const apiEndpoint = `http://localhost:4566/restapis/${apiId}/${stage}/_user_request_`

    const addTask = async () => {
      const task = {
        id: Date.now(),
        name: newTask.value
      }
      await axios.post(`${apiEndpoint}/todos`, task)
      tasks.value.push(task)
      newTask.value = ''
    }

    const deleteTask = async (taskId) => {
      await axios.delete(`${apiEndpoint}/todos/${taskId}`)
      tasks.value = tasks.value.filter((task) => task.id !== taskId)
    }

    onMounted(async () => {
      const response = await axios.get(`${apiEndpoint}/todos`)
      tasks.value = response.data
    })

    return {
      tasks,
      newTask,
      addTask,
      deleteTask
    }
  }
}
</script>
