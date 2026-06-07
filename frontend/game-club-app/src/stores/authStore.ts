import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { jwtDecode } from 'jwt-decode';

export const useAuthStore = defineStore('auth', () => {
    const token = ref<string | null>(localStorage.getItem('accessToken'));
    const userRole = ref<string | null>(null);

    const decodeToken = (jwt: string) => {
        try {
            return jwtDecode<{ role: string }>(jwt);
        } catch (error) {
            return null;
        }
    };

    if (token.value) {
        const decoded = decodeToken(token.value);
        if (decoded && decoded.role) {
            userRole.value = decoded.role;
        }
    }

    const login = (newToken: string) => {
        token.value = newToken;
        localStorage.setItem('accessToken', newToken);
        
        const decoded = decodeToken(newToken);
        if (decoded && decoded.role) {
            userRole.value = decoded.role;
        }
    };

    const logout = () => {
        token.value = null;
        userRole.value = null;
        localStorage.removeItem('accessToken');
    };

    const isAuthenticated = computed(() => !!token.value);
    
    const hasAccess = (allowedRoles: string[]) => {
        if (userRole.value === 'admin') return true;
        return userRole.value ? allowedRoles.includes(userRole.value) : false;
    };

    return { token, userRole, login, logout, isAuthenticated, hasAccess };
});
