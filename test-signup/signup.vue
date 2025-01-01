<script setup>
import { dataStore } from '@/stores/dataStore';

definePageMeta({
   layout: 'main'
})

const isLoading = dataStore().isLoading;
const signUp = dataStore().signUp;

const signUpForm = ref({
   username: '',
   password: ''
})
const formRef = ref(null);

// rules
const rules = ref({
   username: [
      { required: true, message: 'Please input Username', trigger: 'blur' },
      { min: 3, max: 20, message: 'Username should be 3 to 20 characters', trigger: 'blur' }
   ],
   password: [
      { required: true, message: 'Please input Password', trigger: 'blur' },
      { min: 3, max: 20, message: 'Password should be 3 to 20 characters', trigger: 'blur' }
   ],
})

// method handle
const submitForm = () => {
   formRef.value.validate((valid) => {
      if (valid) {
         signUp(signUpForm.value);
      } else {
         console.log('error submit!!');
      }
   });
}
const resetForm = () => {
   formRef.value.resetFields();
}

</script>

<template>

   <el-form
      :model="signUpForm"
      :rules="rules"
      v-loading="isLoading"
      ref="formRef"
      class="signin-form"
      aria-invalid="grammar"
      label-position="top"
   >
      <h1 class="form-title">Sign up</h1>

      <el-form-item
         label="User name"
         prop="username"
      >
         <el-input v-model="signUpForm.username"></el-input>
      </el-form-item>

      <el-form-item
         label="Password"
         prop="password"
      >
         <el-input
            type="password"
            v-model="signUpForm.password"
         ></el-input>
      </el-form-item>

      <el-form-item>
         <el-button
            type="primary"
            size="large"
            @click="submitForm"
            class="signup-btn"
         >Sign up</el-button>
      </el-form-item>

      <p class="signup-text">
         Have an account?
         <nuxt-link
            to="/signin"
            class="signup-link"
         >Sign in</nuxt-link>
      </p>

   </el-form>

</template>

<style scoped>
.signin-form {
   margin-top: 100px;
   padding: 40px;
   height: 400px;
   width: 400px;
   background-color: #09D1C7;
   border-radius: 8px;
   box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
   align-self: center;
}

.form-title {
   text-align: center;
   margin-bottom: 20px;
   color: #000;
}

.el-form-item {
   margin: 20px 0;
}


.signup-btn {
   height: 40px;
   width: 100%;
   /* background-color: #fff; */
}

.signup-btn:hover {
   background-color: aqua;
   color: white;
   transform: scale(1.05)
}

.signup-btn:active {
   background-color: black;
   transform: scale(1);
}


/* Styling for the text */
.signup-text {
   font-size: 1rem;
   color: #000;
   text-align: center;
   margin-top: 1rem;
}

/* Styling for the link */
.signup-link {
   color: #000;
   text-decoration: none;
   font-weight: bold;
   margin-left: 0.2rem;
   transition: color 0.3s ease-in-out;
}

.signup-link:hover {
   color: #048a82;
   /* Darker shade for hover effect */
   text-decoration: underline;
}
</style>
